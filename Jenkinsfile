pipeline {
    agent none 
    stages {
        stage('Build') {
            agent {
                docker {
                    image 'python:3.8.2-alpine3.11'
                }
            }
            steps {
                sh 'python -m py_compile sources/Dealer.py sources/Deck.py sources/ModelView.py sources/Player.py sources/RuleBook.py'
                stash(name: 'compiled-results', includes: 'sources/*.py*')
            }
        }
        stage('Test') { 
            agent {
                docker {
                    image 'python:latest' 
                }
            }
            steps {
                sh 'python sources/UnitTestRuleBook.py'
                sh 'python sources/UnitTestPlayer.py'
                sh 'python sources/UnitTestDeck.py'
                sh 'python sources/UnitTestDealer.py'
                sh 'python sources/IntegrationTests.py'
            }
        }
        stage('Deliver') {
            agent any
            environment {
                VOLUME = '$(pwd)/sources:/src'
                IMAGE = 'cdrx/pyinstaller-linux:python3'
            }
            steps {
                dir(path: env.BUILD_ID) {
                    unstash(name: 'compiled-results')
                    sh "docker run --rm -v ${VOLUME} ${IMAGE} 'pyinstaller -F Dealer.py'"
                }
            }
            post {
                success {
                    archiveArtifacts "${env.BUILD_ID}/sources/dist/blackjack"
                    sh "docker run --rm -v ${VOLUME} ${IMAGE} 'rm -rf build dist'"
                }
            }
        }
    }
}
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
                sh 'python -m py_compile Dealer.py Deck.py ModelView.py Player.py RuleBook.py'
                stash(name: 'compiled-results', includes: '*.py*')
            }
        }
        stage('Test') { 
            agent {
                docker {
                    image 'python:latest' 
                }
            }
            steps {
                sh 'python UnitTestRuleBook.py'
                sh 'python UnitTestPlayer.py'
                sh 'python UnitTestDeck.py'
                sh 'python UnitTestDealer.py'
                sh 'python IntegrationTests.py'
            }
        }
        stage('Deliver') {
            agent any
            environment {
                VOLUME = '$(pwd)/'
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
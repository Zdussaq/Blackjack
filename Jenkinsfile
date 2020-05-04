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
                sh 'py.test --junit-xml test-reports/results.xml UnitTestRuleBook.py'
            }
            post {
                always {
                    junit 'test-reports/results.xml'
                }
            }
        }
    }
}
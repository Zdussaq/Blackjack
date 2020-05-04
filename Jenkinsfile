pipeline {
    agent none 
    stages {
        stage('Test') { 
            agent {
                docker {
                    image 'qnib/pytest' 
                }
            }
            steps {
                sh 'python3 --junit-xml test-reports/results.xml UnitTestRuleBook.py'
            }
            post {
                always {
                    junit 'test-reports/results.xml'
                }
            }
        }
    }
}
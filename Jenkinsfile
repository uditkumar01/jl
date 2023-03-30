// run the python script
pipeline {
    agent any
    stages {
        stage('Build') {
            steps {
                sh 'python ${WORKSPACE}/main.py'
            }
        }
    }
}

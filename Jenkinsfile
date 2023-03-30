// run the python script
pipeline {
    agent any
    stages {
        stage('Build') {
            steps {
                script {
                    def fullPath = "${WORKSPACE}\\main.py"
                    echo fullPath
                    sh "python ${fullPath}"
                }
            }
        }
    }
}

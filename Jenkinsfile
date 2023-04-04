// run the python script
pipeline {
    agent any
    parameters {
        file(name:'FILE', description: 'upload excel file')
    }
    stages {
        stage('Build') {
            steps {
                // script {
                //     def fullPath = "${WORKSPACE}\\main.py"
                //     echo fullPath
                    
                // }
                // sh "export TERM=xterm-color"
                bat "export TERM=xterm-color"
                bat 'pip install -r requirements.txt'
                bat '"C:\\Program Files\\Python310\\python.exe" "C:\\Users\\kumaru\\projects\\jenkins-proj\\main.py"'
                writeFile(file: 'file.csv', text: readFile(FILE))  
            }
        }
    }
}

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
                bat '"C:\\Program Files\\Python310\\python.exe" "C:\\Users\\kumaru\\projects\\jenkins-proj\\main.py"'
                writeFile file: 'file.csv', text: readFile(FILE)     
            }
        }
    }
}

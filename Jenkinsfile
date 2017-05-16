pipeline {
    agent any

    stages {
        stage("Buildenv") {
            steps {
                echo "Building build env.."
                sh "virtualenv python"
                sh "python/bin/pip install pyinstaller"
            }
        }
        stage("Build") {
            steps {
                echo "Building TicTacToe.."
                sh "python/bin/pyinstaller client.py"
            }
        }
    }
}

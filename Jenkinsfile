pipeline {
    agent any


    stages {
        stage("Clean") {
            steps {
                echo "cleaning.."
                sh "rm * -rf"
                checkout scm
            }
        }
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
        stage("Archive") {
            steps {
                echo "Building artifacts.."
                sh "mv game dist/game"
                archiveArtifacts artifacts: 'dist/*', fingerprint: true
                echo "Cleanup.."
                sh "rm Jenkinsfile LICENSE README.md build client.py client.spec python -rf"
            }
        }
    }
}

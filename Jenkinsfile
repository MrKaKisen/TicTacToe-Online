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
                sh "python/bin/pyinstaller --onefile client.py"
            }
        }
        stage("Archive") {
            steps {
                echo "Building artifacts.."
                sh "mv dist/client dist/TicTacToe-Online-${BUILD_NUMBER}"
                archiveArtifacts artifacts: 'dist/TicTacToe-Online-${BUILD_NUMBER}', fingerprint: true
                echo "Cleanup.."
                sh "rm * -rf"
            }
        }
    }
}

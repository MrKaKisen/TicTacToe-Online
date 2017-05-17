pipeline {
    agent any
    stages {
        stage("Clean") {
            steps {
                /* bad way to get commit id :) */
                sh "git rev-parse --short HEAD > .git/commit-id"
                commit_id = readFile('.git/commit-id')
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
                sh "mv dist/client dist/TicTacToe-Online-${commit_id}"
                archiveArtifacts artifacts: 'dist/TicTacToe-Online-${commit_id', fingerprint: true
                echo "Cleanup.."
                sh "rm * -rf"
            }
        }
    }
}

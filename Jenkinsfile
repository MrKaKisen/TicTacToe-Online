pipeline {
    agent any

    stages {
        stage("Buildenv") {
            steps {
                echo "Building build env.."
                sh "virtualenv python"
                sh "python/bin/pip install py2exe"
            }
        }
        stage("Build") {
            steps {
                echo "Building TicTacToe.."
                sh "python/bin/python setup.py py2exe"
            }
        }
    }
}

pipeline {
    agent any

    environment {
        DOCKERHUB_CREDENTIALS = 'dockerhub-credentials-id'
        IMAGE_NAME = 'adrshthakur8368/sentiment-analysis-app'
        IMAGE_TAG = 'latest'
    }

    stages {
        stage('Clone Repo') {
            steps {
                git 'https://github.com/Adarshthakur-850/sentiment-analysis-app.git'
            }
        }

        stage('Build Image') {
            steps {
                script {
                    echo "Building Docker Image: ${IMAGE_NAME}:${IMAGE_TAG}"
                    docker.build("${IMAGE_NAME}:${IMAGE_TAG}")
                }
            }
        }

        stage('Login and Push') {
            steps {
                script {
                    echo "Logging in and pushing image"
                    docker.withRegistry('https://index.docker.io/v1/', "${DOCKERHUB_CREDENTIALS}") {
                        docker.image("${IMAGE_NAME}:${IMAGE_TAG}").push()
                    }
                }
            }
        }
    }

    post {
        failure {
            echo '❌ Build failed. Check logs above for details.'
        }
        success {
            echo '✅ Build and push succeeded.'
        }
    }
}

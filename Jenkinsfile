pipeline {
    agent any

    environment {
        DOCKERHUB_CREDENTIALS = 'dockerhub-credentials-id' // Replace with your Jenkins DockerHub credential ID
        IMAGE_NAME = 'adrshthakur8368/sentiment-analysis-app'
        IMAGE_TAG = 'latest'
    }

    stages {
        stage('Clone Repo') {
            steps {
                git 'https://github.com/Adarshthakur-850/sentiment-analysis-app.git'
            }
        }

        stage('Build Docker Image') {
            steps {
                script {
                    docker.build("${IMAGE_NAME}:${IMAGE_TAG}")
                }
            }
        }

        stage('Login to Docker Hub') {
            steps {
                script {
                    docker.withRegistry('https://index.docker.io/v1/', "${DOCKERHUB_CREDENTIALS}") {
                        echo 'Logged in to Docker Hub'
                    }
                }
            }
        }

        stage('Push Image') {
            steps {
                script {
                    docker.withRegistry('https://index.docker.io/v1/', "${DOCKERHUB_CREDENTIALS}") {
                        def customImage = docker.image("${IMAGE_NAME}:${IMAGE_TAG}")
                        customImage.push()
                    }
                }
            }
        }
    }

    post {
        always {
            echo 'Pipeline execution finished.'
        }
    }
}

pipeline {
    agent any
    environment {
        DOCKER_APP_IMAGE = "ankurpatel/flaskapp" + ":$BUILD_NUMBER"
        DOCKER_DB_IMAGE = "ankurpatel/db" + ":$BUILD_NUMBER"
        registryCredential = 'Docker_Hub_Login'
        
    }

    stages {

        stage('Cloning Git') {
            steps {
              git 'https://github.com/patel0ankur/k8_cicd.git'
                }
            }

        stage('Build DB Docker Image'){
            when {
                branch 'master'
            }
            steps {
                script {
                db = docker.build(DOCKER_DB_IMAGE, "-f db/Dockerfile db/")
                }
            }
        }

        stage('Build APP Docker Image') {
            when {
                branch 'master'
            }
            steps {
                script {
                    app = docker.build(DOCKER_APP_IMAGE, "-f app/Dockerfile app/")
                   }
            }
        }

        stage('Push DB Docker Image') {
            when {
                branch 'master'
            }
            steps {
                script {
                    docker.withRegistry('https://registry.hub.docker.com', registryCredential ) {
                        db.push("$BUILD_NUMBER")
                    }
                }
            }
        }

        stage('Push APP Docker Image') {
            when {
                branch 'master'
            }
            steps {
                script {
                    docker.withRegistry('https://registry.hub.docker.com', registryCredential ) {
                        app.push("$BUILD_NUMBER")
                    }
                }
            }
        }

         stage('Deploy DB To K8s') {
            when {
                branch 'master'
            }
            steps {
                milestone(1)
                kubernetesDeploy(
                    kubeconfigId: 'kubeconfig',
                    configs: 'db/mysql_deployment.yml',
                    enableConfigSubstitution: true
                )
            }
        }

        stage('Deploy APP To K8s') {
            when {
                branch 'master'
            }
            steps {
                milestone(1)
                kubernetesDeploy(
                    kubeconfigId: 'kubeconfig',
                    configs: 'app/flaskapp_deployment.yml',
                    enableConfigSubstitution: true
                )
            }
        }
    }
}

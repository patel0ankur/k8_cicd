pipeline {
  agent any
  stages {
    stage('Build Images') {
      parallel {
        stage('Build App Image') {
          agent any
          steps {
            sh '''ls
sudo docker build -t ankurpatel/flaskapp:latest app/
'''
          }
        }
        stage('Build DB Image') {
          steps {
            sh '''ls
sudo docker build -t ankurpatel/flaskdb:latest db/'''
          }
        }
      }
    }
    stage('Push Images') {
      steps {
        sh '''sudo docker push ankurpatel/flaskapp:latest
sudo docker push ankurpatel/flaskdb:latest'''
      }
    }
    stage('Deploy') {
      steps {
        sh 'sudo docker stack deploy -c docker_stack.yml flaskapp'
      }
    }
    stage('Test Website') {
      steps {
        sh 'curl -Is http://127.0.0.1:5000 | head -n1'
      }
    }
  }
}
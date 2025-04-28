pipeline {
  agent any
  stages {
    stage('Build') {
      steps {
        sh 'docker build -t monitor-app .'
      }
    }
    stage('Test') {
      steps {
        sh 'docker run --rm monitor-app | grep "App Status"'
      }
    }
    stage('Deploy') {
      steps {
        sh 'docker run -d -p 5000:5000 monitor-app'
      }
    }
  }
}

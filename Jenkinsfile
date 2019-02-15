pipeline {
  agent {
    node {
      label 'stage-1'
    }

  }
  stages {
    stage('stage-1') {
      steps {
        echo 'hi'
      }
    }
    stage('stage-2') {
      steps {
        echo 'wassup'
      }
    }
    stage('stage-3') {
      steps {
        echo 'bye'
      }
    }
  }
}
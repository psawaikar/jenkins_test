node {

    stage('Clone Repo') {
        checkout scm

    }

    stage('Build') {
        //echo "Hello World"
        //app1 = docker.image('psawaikar/jenkinstestdimage')
        docker.image('alpine:latest').inside {
        sh 'echo Hello World!'
        }
    }

}
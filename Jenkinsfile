node {
    def app1

    stage('Clone Repo') {
        checkout scm

    }

    stage('Build') {
        //echo "Hello World"
        app1 = docker.build('psawaikar/jenkinstestdimage')
        //docker.image('alpine:latest').inside {
        //sh 'echo Hello World!'
        //}
    }

}
node {

    def app1

    stage('Clone Repo') {
        checkout scm
    }

    stage('Build') {
        app1 = docker.image('psawaikar/jenkinstestdimage')
    }

}
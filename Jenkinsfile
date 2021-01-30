node {

    def app1

    stage('Clone Repo') {
        checkout scm
    }

    stage('Build') {
        echo "Hello World"
        app1 = docker.image('psawaikar/jenkinstestdimage')
    }

}
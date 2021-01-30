node {
    def app1

    stage('Clone Repo') {
        checkout scm
    }

    stage('Dev') {
        //echo "Hello World"
        app1 = docker.build('psawaikar/jenkinstestdimage')

        //**** Unit Testing of each docker image goes here -- ADD LATER

        //docker.image('alpine:latest').inside {
        //sh 'echo Hello World!'
        //}
    }

    stage('BAT') {
        //**** BAT tests to be run here -- ADD LATER
        app1.push()
    }

    stage('QA') {
        //**** QA tests to be run here -- ADD LATER
        echo "QA Stage - TBD LATER"
    }





}
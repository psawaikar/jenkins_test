node {
    //def app1
    def dockerTag
    def dockerImageStr
    def dockerhubRepo = "psawaikar/testjenkins"
    def dockerImage

    def dockerHubRegistry = 'https://registry.hub.docker.com/'
    def dockerHubID = 'psawaikar-DockerHub'

    def gitTag
    def buildNo

    stage('Checkout') {
        checkout scm

        gitTag = gitTagName()
        sh "echo ${gitTag} "

        dockerTag = getDockerTagfromGitTag(gitTag)
        //sh "echo hello"
        sh "echo ${dockerTag}"
        buildNo = dockerTag



//tag=$( echo $name | cut -d'-' -f2 )
//echo $tag
    }

    stage('Dev') {
        //echo "Hello World"

        dockerImageStr = dockerhubRepo + ":" + dockerTag
        sh "echo ${dockerImageStr}"

        dockerImage = docker.build(dockerImageStr)

        //**** Unit Testing of each docker image goes here -- ADD LATER

        //docker.image('alpine:latest').inside {
        //sh 'echo Hello World!'
        //}
    }

    stage('BAT') {
        //**** BAT tests to be run here -- ADD LATER


       //Convert dev-docker-compose to qa-docker-compose


        docker.withRegistry(dockerHubRegistry, dockerHubID) {

            dockerImage.push(dockerTag)
       }

       def baseS3folder = "s3://ambuilds/testbuild/"
       def destS3folder = baseS3folder + buildNo + "/"

       withCredentials([[$class: 'AmazonWebServicesCredentialsBinding', accessKeyVariable: 'AWS_ACCESS_KEY_ID', credentialsId: 'aws-parag', secretKeyVariable: 'AWS_SECRET_ACCESS_KEY']]) {
         //sh "aws s3 ls"

         sh "aws s3 cp ${workspace}/build-qa.yml ${destS3folder}"
        }

        def workspace = WORKSPACE
        // ${workspace} will now contain an absolute path to job workspace on slave

        workspace = env.WORKSPACE

        // When using a GString at least later Jenkins versions could only handle the env.WORKSPACE variant:
        echo "Current workspace is ${env.WORKSPACE}"




       // withCredentials([[$class: 'AmazonWebServicesCredentialsBinding', accessKeyVariable: 'AWS_ACCESS_KEY_ID', credentialsId: 'aws-parag', secretKeyVariable: 'AWS_SECRET_ACCESS_KEY']]) {
       //  sh "aws s3 ls"
       //  sh "aws s3 cp ${workspace} s3://ambuilds/testbuild --recursive"


       //  }


    }

    stage('QA') {
        //**** QA tests to be run here -- ADD LATER
        echo "QA Stage - TBD LATER"
    }

}
/** @return The tag name, or `null` if the current commit isn't a tag. */
String gitTagName() {
    commit = getCommit()
    if (commit) {
        desc = sh(script: "git describe --tags ${commit}", returnStdout: true)?.trim()
        if (isTag(desc)) {
            return desc
        }
    }
    return null
}

/** @return The tag message, or `null` if the current commit isn't a tag. */
String gitTagMessage() {
    name = gitTagName()
    msg = sh(script: "git tag -n10000 -l ${name}", returnStdout: true)?.trim()
    if (msg) {
        return msg.substring(name.size()+1, msg.size())
    }
    return null
}

String getCommit() {
    return sh(script: 'git rev-parse HEAD', returnStdout: true)?.trim()
}

@NonCPS
boolean isTag(String desc) {
    match = desc =~ /.+-[0-9]+-g[0-9A-Fa-f]{6,}$/
    result = !match
    match = null // prevent serialisation
    return result
}

String getDockerTagfromGitTag(String gittag) {
    tags = gittag.split('-')
    return tags[1]
}



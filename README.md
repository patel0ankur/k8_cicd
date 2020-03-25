# k8_cicd
Prepare the Jenkins Environment and Verify Your Configuration with an Initial Deploy:

1) Add GitHub Credentials in Jenkins:

We will use a GitHub API token:

a. Navigate to the GitHub tab in your browser.

b. Click your profile picture in the top right of the page, click Settings,  click Developer settings, click Personal access tokens, and finally click Generate new token.

    • Name this token "jenkins_token" and be sure to click the checkbox next to admin:repo_hook. 

    • Click Generate token at the bottom of the page. Copy the token to your clipboard.

c. Back in the Jenkins tab in your browser, click Credentials in the menu. Click Add Credentials. 

    • Username: Provide your GitHub username

    • Password: Paste the API token from your clipboard.

    • ID: github_key

    • Description: GitHub Key

d. Click OK.

2) Add DockerHub Credentials in Jenkins:

a. Click Add Credentials in the menu on the left of the page.

    • Username: Provide your DockerHub username

    • Password: Provide your DuckerHub password
    
    • ID: docker_hub_login
    
    • Description: Docker Hub Login

b. Click OK.


3) Add the Kubeconfig from the Kubernetes master as a credential in Jenkins:

a. Log in to the Kubernetes master node.

b. Display the contents of our Kubeconfig:

    • cat ~/.kube/config

c. Copy the output of this file to your clipboard. We will need to paste this into Jenkins.

d. Click Add Credentials in the menu on the left of the page.

e. Add credentials with the following information:

    • Kind: Kubernetes configuration (kubeconfig)

    • ID: kubeconfig

    • Description: Kubeconfig

    • Kubeconfig: Enter directly

    • Content: Paste the contents of ~/.kube/config

f. Click OK.


4) Configure Environment Variables:

a. On the main page of Jenkins, click Manage Jenkins. Click Configure System.

b. In the Global Properties section, click the checkbox next to Environment variables. Click Add.

  • Name: KUBE_MASTER_IP

  • Value: <ip>

c. Click Apply.

d. In the GitHub section, click Add GitHub Server and then click GitHub Server.

	• Name: GitHub

 	• Credentials: Click Add and then click Jenkins

		○ Kind: Secret text

		○ Secret: Paste the GitHub API token from the earlier step

		○ ID: github_secret

		○ Description: GitHub Secret

e. Click Add. Click the dropdown next to Credentials and select the GitHub Secret we just added. Click Save.

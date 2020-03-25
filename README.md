# k8_cicd
Prepare the Jenkins Environment and Verify Your Configuration with an Initial Deploy:

Add GitHub Credentials in Jenkins:

We will use a GitHub API token:

1. Navigate to the GitHub tab in your browser.

2. Click your profile picture in the top right of the page, click Settings,  click Developer settings, click Personal access tokens, and finally click Generate new token.

    • Name this token "jenkins_token" and be sure to click the checkbox next to admin:repo_hook. 

    • Click Generate token at the bottom of the page. Copy the token to your clipboard.

3. Back in the Jenkins tab in your browser, click Credentials in the menu. Click Add Credentials. 

    • Username: Provide your GitHub username

    • Password: Paste the API token from your clipboard.

    • ID: github_key

    • Description: GitHub Key

4. Click OK.

Add DockerHub Credentials in Jenkins:

1. Click Add Credentials in the menu on the left of the page.

    • Username: Provide your DockerHub username

    • Password: Provide your DuckerHub password
    
    • ID: docker_hub_login
    
    • Description: Docker Hub Login

2. Click OK.

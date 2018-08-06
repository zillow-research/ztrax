# how to setup rstudio server on google cloud
# following http://grantmcdermott.com/2017/05/30/rstudio-server-compute-engine/

1. get gcloud [SDK](https://cloud.google.com/sdk/)
1. have python 2.7.10
1. be logged into google.com with your primary email
1. set project and zone:
	1. `gcloud config set project "your-project-name"`
1. reserve a static IP: `gcloud compute addresses create zillow-ip --region us-east1`
1. create a new instance and assign IP address to it:
	```gcloud compute instances create rstudio --image-family ubuntu-1604-lts --image-project ubuntu-os-cloud  --machine-type n1-standard-8 --address zillow-ip --region us-east1```
1. Allow inward traffic to port 8787: `gcloud compute firewall-rules create allow-rstudio --allow=tcp:8787`
1. log into machine: `gcloud compute ssh rstudio`
1. Follow [R instructions](https://cran.rstudio.com/bin/linux/ubuntu/README.html) to install ubuntu packages
1. Follow [Rstudio instructions to install server](https://www.rstudio.com/products/rstudio/download-server/)
1. open a browser and navigate to `https://35.229.67.163:8787`




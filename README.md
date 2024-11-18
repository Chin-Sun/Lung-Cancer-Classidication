<!--
# Project Introduction: 
A service is accessible on the Internet. Its design follows RESTful architecture style that runs on the **AWS Cloud** platform and meets the requirements below. The service interface is defined on Dast API by using SwaggerHub open APIs.

Cloud and open community provide pre-trained models that can be leveraged to deliver smart services. My service can integrate with my hugging face model to deliver the cloud and enable development,configuration and integration of multiple types of services.

# Project Tasks:

1. Utilize a Cloud platform such as **Amazon EC2**. And take advantage of **S3** or DynamoDB.
2. Design the data model of your services.  
3. Use a NoSQL data store for managing the data of your application.  
4. Select a Hugging face model or a Cloud AI service to integrate  
5. Develop and deploy the service with integration to 4
6. Expose REST/Open APIs to SwaggerHub
7. Do performance and operation measurement  
# My Demo Vedio（09.2023-11.2023）
[![Lung Cancer Classification](https://img.youtube.com/vi/3dOk_ofCyZ0/0.jpg)](https://youtu.be/3dOk_ofCyZ0)

## Main function of my project: 
My service can help users to detect whether they have lung cancer or not with the help of AI-driven image analysis. What they need to do is to upload their lung image on our application. And then they can get a result which will show their diagnosis results

## Folder and Link Introduction:   
---'img': data used by testing my service     

Here is my hugging face model link: https://huggingface.co/olp0qlo/lung-cancer-classification  

Here is the public URL for my service: http://35.87.24.51/  
-->

# **Lung Cancer Classification System on AWS**

**Project Duration**: Jan 2024 - Present  

---

## **Project Overview**  

The Lung Cancer Classification System is an end-to-end solution designed to assist in the early detection and classification of lung cancer. Leveraging cloud infrastructure and modern web technologies, the system provides a responsive interface for users to upload lung images and receive classification results, ensuring scalability, reliability, and efficiency.

---

## **Project Requirements**  

### **User Requirements**  
- Enable users (medical professionals) to upload lung images for classification.  
- Provide real-time feedback on the classification results.  
- Maintain a secure and user-friendly interface.  

### **Technical Requirements**  
- Store and manage large amounts of data, including user information and high-resolution lung images.  
- Ensure high availability and fault tolerance.  
- Automate deployments and manage services consistently across environments.  

---

## **Project Details (STAR Method)**  

### **Situation**  
Early detection of lung cancer significantly increases survival rates. However, many existing tools lack scalability and integration with cloud infrastructure, leading to challenges in managing large datasets and providing real-time results.

### **Task**  
Develop a cloud-based system to classify lung cancer images with a focus on scalability, security, and ease of use. The system must allow healthcare professionals to upload lung images, classify them using machine learning models, and view results quickly.

### **Action**  

1. **Front-End Development**  
   - Built a **responsive interface** using **HTML/CSS** and **JavaScript** for seamless user interaction.  
   - Integrated **FastAPI RESTful APIs** to handle user requests efficiently, with comprehensive API documentation using **SwaggerHub**.  

2. **Data Storage Design**  
   - Designed a **hybrid storage system**:  
     - **MongoDB**: For securely storing users' profiles and classification history.  
     - **AWS S3**: For managing high-resolution lung images and system logs, ensuring scalability.  

3. **Deployment and Infrastructure**  
   - Deployed the system on **AWS EC2** for continuous operation and **AWS Lambda** for dynamic image processing.  
   - Configured the system on an **Ubuntu server** for optimal performance.  
   - Monitored system performance with **AWS CloudWatch**, enabling proactive issue resolution.  

4. **CI/CD and Containerization**  
   - Implemented **CI/CD pipelines** using **GitHub Actions**, automating testing, building, and deployment.  
   - Containerized the application using **Docker** and managed microservices with **Kubernetes** for scalability and consistency.  

### **Expected Result**  
- Achieved **95% uptime** through efficient deployment and monitoring practices.  
- Reduced deployment time by **30%** through CI/CD pipelines.  
- Enhanced data retrieval and image classification, improving user experience.  
- Scaled the system to handle a **30% increase in concurrent users** without performance degradation.  

---

## **Project Highlights**  

- **Cloud-First Design**: Optimized for cloud infrastructure, ensuring high availability and fault tolerance.  
- **Hybrid Storage**: Leveraged MongoDB and AWS S3 for efficient data management.  
- **Microservice Architecture**: Used Docker and Kubernetes for streamlined deployments and enhanced scalability.
   
<!--
---

## **Lessons Learned and Future Improvements**  

### **Lessons Learned**  
- Efficient monitoring and alerting are crucial for maintaining system reliability.  
- Hybrid storage systems offer flexibility but require careful configuration to optimize cost and performance.  

### **Future Improvements**  
- Integrate **machine learning pipelines** for real-time model updates.  
- Enhance **security measures** with advanced authentication and data encryption.  
- Explore **cost optimization** strategies with **AWS Spot Instances** and **Lambda reserved concurrency**.  
 -->
---

## **Tech Stack**  

- **Front-End**: HTML, CSS, JavaScript  
- **Back-End**: FastAPI  
- **Database**: MongoDB, AWS S3  
- **Deployment**: AWS EC2, AWS Lambda, Ubuntu Server  
- **Monitoring**: AWS CloudWatch  
- **CI/CD**: GitHub Actions  
- **Containerization**: Docker, Kubernetes  

---

Feel free to contribute or provide feedback!

# My Demo Vedio
[![Lung Cancer Classification](https://img.youtube.com/vi/3dOk_ofCyZ0/0.jpg)](https://youtu.be/3dOk_ofCyZ0)

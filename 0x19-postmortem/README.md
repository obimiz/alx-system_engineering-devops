Issue Summary
Duration of the outage: 2 hours, from 2:00 PM to 4:00 PM UTC on June 12, 2024.
 
Impact: Our web application, jimakadultedu.com.ng, was experiencing slow response times and intermittent errors, affecting approximately 40% of our users during the outage period. 

Root Cause: A configuration change in our load balancer resulted in an uneven distribution of traffic across the application servers, leading to some servers being overwhelmed while others were underutilized.

Timeline
2:05 PM - The issue was detected through monitoring alerts indicating high CPU and memory usage on a subset of the application servers.
2:10 PM - The on-call engineer investigated the application logs and noticed a spike in error rates and slow response times.
2:20 PM - The engineering team was notified, and initial investigations focused on potential issues with the application code or database.
2:45 PM - After ruling out application and database issues, the team shifted their focus to the infrastructure layer.
3:00 PM - The incident was escalated to the infrastructure team, who discovered a recent load balancer configuration change.
3:30 PM - The infrastructure team reverted the load balancer configuration change, and the issue started to resolve gradually.
4:00 PM - The system stabilized, and response times returned to normal levels.

Root Cause and Resolution
The root cause of the issue was a misconfigured load balancer rule that resulted in an uneven distribution of traffic across the application servers. Specifically, a recent change in the load balancer configuration caused a subset of servers to receive a disproportionately high volume of traffic, leading to resource exhaustion and slow response times.
To resolve the issue, the infrastructure team reverted the load balancer configuration to its previous state, restoring the even distribution of traffic across all application servers.

Corrective and Preventative Measures
Areas for improvement:
Load balancer configuration changes should be thoroughly tested and validated before deployment.
Monitoring and alerting systems should be enhanced to provide better visibility into load balancer health and traffic distribution.
Incident response procedures should be streamlined for faster escalation and resolution.

Specific tasks:
Implement a comprehensive load testing and validation process for load balancer configuration changes.
Set up monitoring and alerting for load balancer traffic distribution metrics.
Review and update the incident response playbook to include load balancer-related issues.
Conduct a post-mortem review with the relevant teams to identify additional areas for improvement.
Schedule training sessions for the engineering team on load balancer configuration and troubleshooting.



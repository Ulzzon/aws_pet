# My reflections of this project
I will try to gather my thoughts of the projects at different points, kind of release notes but reflections of functionalities and potential improvements. 

## 2020-11-20
The construct is all about setting up the right conditions for the lambda to work with and to my understanging is only executed at cold start while the lambda code "hitcount.py" is only executed up on request. So the actual logic rest inside the lambda code and the construct is the initialization phase to ensure the lambda has the right permissions and dependencies for the actual execution to take place. 


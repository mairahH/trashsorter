# TrashSorter  
### **Putting Trash in Its Place**

The TrashSorter is a machine designed to make recycling easier and more efficient by automating the sorting process using image recognition and hardware integration. The project aims to tackle the growing issue of improper waste management and recycling inefficiencies.

---

## **Overview**  

Recycling is crucial to reducing environmental damage, yet improper sorting often renders waste unrecyclable. TrashSorter addresses this by leveraging:
- **Image recognition** powered by a custom machine learning model.
- **Arduino-based hardware** to detect and classify objects.
- A **rotating platform** to direct items to their respective bins.

---

## **Features**  
- **Image Recognition**: Built using the Clarifai API to classify recyclable and non-recyclable materials.  
- **Hardware Integration**: Arduino Uno, ultrasonic sensors, and servo motors work together to control sorting actions.  
- **Data Collection**: Processes and analyzes input data to improve model accuracy.  

---

## **Materials**  
The following components were used in building the TrashSorter:  
- **Hardware**: Arduino Uno, ultrasonic sensor, breadboard, servo motor, jumper wires, webcam, foam board, wooden stick, bins.  
- **Software**: Python, Clarifai API, Tinkercad for circuit modeling.  

---

## **How It Works**  
1. **Detection**: An ultrasonic sensor identifies the presence of an item.  
2. **Classification**: The camera captures an image of the item, which is processed through a Clarifai-based image recognition model.  
3. **Sorting**: A servo motor rotates the platform to deposit the item into either the recyclable or non-recyclable bin.  

---

## **Results and Accuracy**  
Initial experiments yielded an average accuracy of **47%**, with plans to improve through additional training and data collection. Future iterations aim to achieve near-perfect sorting accuracy.  

---

## **Setup and Usage**  
### Hardware Setup:  
1. Connect the Arduino Uno to the ultrasonic sensor, servo motor, and webcam via the breadboard.  
2. Attach the servo motor to the rotating platform.  

### **Project Insights**
This project demonstrates the integration of machine learning with hardware systems to solve a real-world problem.
Areas for improvement include increasing training data for the model and enhancing hardware stability.

### **Future Work**
- Train the image recognition model with additional datasets for improved accuracy.
- Replace the current webcam with a high-resolution camera for better image quality.
- Refine hardware design to ensure durability and consistency.

## References
- [Clarifai API Documentation](https://clarifai.com)
- [Arduino Circuit Resources](https://www.circuito.io/blog/arduino-sensors-explained/)

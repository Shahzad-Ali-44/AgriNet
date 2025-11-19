# AgriNet - AI Powered Corn Leafs Disease Detection

AgriNet is an AI-powered web application designed to detect early corn crop diseases and provide effective treatment recommendations. This innovative solution helps farmers improve crop health and yield by leveraging deep learning models.

##  Features

- **AI-Powered Detection:** Achieves 94% accuracy using a VGG-19 model for early disease identification.
- **Treatment Recommendations:** Offers actionable insights for disease management.
- **Fully Responsive:** Optimized for seamless usage across all devices.
- **Contact Form:** A fully functional form to get in touch with us.
- **Newsletter Subscription:** Stay informed with the latest agricultural updates.


##  Installation and Setup

Clone the repository:
   ```bash
   git clone https://github.com/Shahzad-Ali-44/AgriNet.git
   ```


### Frontend (Next.js)

1. Install dependencies:
   ```bash
   npm install
   ```

2. Run the development server:
   ```bash
   npm run dev
   ```

### Backend (FastAPI)

#### Required Dependencies

If you have only Python installed, you'll need to install the following libraries:

- `fastapi`
- `uvicorn`
- `numpy`
- `pillow`
- `tensorflow`
- `logging`

To install them, run:

```bash
pip install fastapi uvicorn numpy pillow tensorflow logging
```

To start the backend server:

```bash
python main.py
```

### Model File Setup with Git LFS

The VGG-19 model file (`vgg19_model.keras`) exceeds GitHub's file size limit and is tracked using Git LFS. To clone and use the repository with the model:

1. Install Git LFS:
   ```bash
   git lfs install
   ```

2. Pull the model file using Git LFS:
   ```bash
   git lfs pull
   ```
## Contact Form Configuration

To enable the contact form functionality, follow these steps:

1. **Get an Access Key**:
   - Visit [Web3Forms](https://web3forms.com/) and sign up to get your free access key.

2. **Update the `.env.local` File**:
   - Add the following entry to your `.env.local` file:
     ```env
     NEXT_PUBLIC_AccessKey=your-access-key-here
     ```

3. **How It Works**:
   - The contact form uses the Web3Forms API to send messages to the email address you configure in your Web3Forms account.
   - Ensure your application has internet access to communicate with the Web3Forms API.


##  Usage

1. Upload an image of the corn crop.
2. The AI model will analyze and detect potential diseases.
3. Receive treatment suggestions and actionable insights.

##  Technology Stack

- **Frontend:** Next.js
- **Backend:** FastAPI
- **Model:** Visual Geometry Group (VGG-19) with 94% accuracy

##  Contributing

Contributions are welcome! Feel free to fork the repository, make improvements, and submit a pull request.

##  License

This project is licensed under the [MIT License](LICENSE).

## Acknowledgments

- Dataset contributors for their valuable efforts.
- TensorFlow and Keras for their robust deep learning frameworks.
- Open-source community for tools and libraries enabling this work.

*🌾 AgriNet - AI Powered Corn Leafs Disease Detection.*


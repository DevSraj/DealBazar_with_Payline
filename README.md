# DealBazar with Payline

Welcome to DealBazar, an e-commerce frontend website built using React. This project is designed to provide a seamless shopping experience for users, featuring a modern and responsive design.It also integrates our own blockchain based payment gateway, Payline. Integrates AI features for fraud detection and prevention. This README file will guide you through the setup, installation, and usage of this project.

## Demo

You can check out the live demo of the Shopper website [here](#).

## Features

- Responsive design of website for optimal viewing on any device
- Full control over blockain being used
- Powerful and efficient AI integration 
- Own cryptocurrency
- Various fraud detection and preventive measure

## Technologies Used

- React
- Redux (for state management)
- React Router (for navigation)
- Styled-components (for styling)
- Firebase (for authentication and database)
- Stripe (for payment processing)

## Installation

To get a local copy up and running, follow these simple steps.

### Prerequisites

Make sure you have the following installed:

- Node.js (v14 or later)
- npm (v6 or later) or yarn (v1.22 or later)

### Clone the Repository

```sh
git clone https://github.com/your-username/DealBazar_with_Payline.git
cd shopper
```

### Install Dependencies

Using npm:

```sh
npm install
```

Or using yarn:

```sh
yarn install
```

## Usage

To start the development server, run:

Using npm:

```sh
npm start
```

Or using yarn:

```sh
yarn start
```

This will launch the app on `http://localhost:3000`. Open your browser and navigate to this URL to see the application in action.

### Building for Production

To build the project for production, run:

Using npm:

```sh
npm run build
```

Or using yarn:

```sh
yarn build
```

This will create an optimized build of the app in the `build` directory.

### Firebase Configuration

1. Create a Firebase project at [Firebase Console](https://console.firebase.google.com/).
2. Add a new web app to your project.
3. Copy the Firebase config object.
4. Create a `.env` file in the root of the project and add your Firebase configuration:

```sh
REACT_APP_FIREBASE_API_KEY=your_api_key
REACT_APP_FIREBASE_AUTH_DOMAIN=your_auth_domain
REACT_APP_FIREBASE_PROJECT_ID=your_project_id
REACT_APP_FIREBASE_STORAGE_BUCKET=your_storage_bucket
REACT_APP_FIREBASE_MESSAGING_SENDER_ID=your_messaging_sender_id
REACT_APP_FIREBASE_APP_ID=your_app_id
```

### Stripe Configuration

1. Create a Stripe account at [Stripe](https://stripe.com/).
2. Obtain your publishable and secret keys from the Stripe Dashboard.
3. Add your Stripe keys to the `.env` file:

```sh
REACT_APP_STRIPE_PUBLIC_KEY=your_stripe_public_key
```

## Contributing

Contributions are what make the open source community such an amazing place to learn, inspire, and create. Any contributions you make are **greatly appreciated**.

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## License

Distributed under the MIT License. See `LICENSE` for more information.

---

Feel free to explore and contribute to the project. For any questions or issues, please open an issue on GitHub.

Happy coding! 🚀

---

**Note:** Replace the placeholder links and texts (e.g., `https://github.com/your-username/shopper.git`, `your_api_key`) with the actual information related to your project.

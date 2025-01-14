import './App.css'
import Layout from './Layout';
import { BrowserRouter, Navigate } from "react-router-dom";
import { useRoutes } from "react-router-dom";
import Chat from './pages/Chat/Chat';
function AppRoutes() {
  const routes = [
    {
      path: "/",
      element: <Layout />,
      children: [
        { path: "/", element: <Navigate to="/chat" replace /> },
        { path: "chat", element: <Chat /> },
      ],
    },
  ];

  return useRoutes(routes);
}

function App() {
  return (
    <BrowserRouter>
      <AppRoutes />
    </BrowserRouter>
  );
}

export default App;
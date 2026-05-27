import { Routes, Route } from "react-router-dom";

import Register from "./pages/Register";
import Login from "./pages/Login";
import Dashboard from "./pages/Dashboard";
import ProtectedRoute from "./routes/ProtectedRoute";
import PublicRoute from "./routes/PublicRoute";

function App() {
  return (
    <Routes>
      <Route path="/dashboard" element={<ProtectedRoute> <Dashboard/> </ProtectedRoute>}/>
      <Route path="/login" element={<PublicRoute> <Login/> </PublicRoute>}/>
      <Route path="/register" element={<PublicRoute> <Register/> </PublicRoute>}/>
    </Routes>
  )
}

export default App
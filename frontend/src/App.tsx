import { Routes, Route, Navigate } from "react-router-dom";

import Register from "./pages/Register";
import Login from "./pages/Login";
import Projects from "./pages/Projects";
import Scans from "./pages/Scans";
import Reports from "./pages/Reports";

import Dashboard from "./pages/Dashboard";

import AppLayout from "./layouts/AppLayout";

import ProtectedRoute from "./routes/ProtectedRoute";
import PublicRoute from "./routes/PublicRoute";

function App() {
  return (
    <Routes>
      <Route path="/login" element={<PublicRoute> <Login/> </PublicRoute>}/>
      <Route path="/register" element={<PublicRoute> <Register/> </PublicRoute>}/>

      <Route element={<ProtectedRoute> <AppLayout/> </ProtectedRoute>}>
        <Route path="/dashboard" element={<ProtectedRoute> <Dashboard/> </ProtectedRoute>}/>
        <Route path="/projects" element={<Projects />}/>
        <Route path="/scans" element={<Scans />}/>
        <Route path="/reports" element={<Reports />}/>
      </Route>

      <Route path="*" element={<Navigate to="login"/>}></Route>
    </Routes>
  )
}

export default App
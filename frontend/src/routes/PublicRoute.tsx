import { Navigate } from "react-router-dom";
import { useAuth } from "../context/AuthContext";

type PublicRouteProps = {
    children : React.ReactNode
}

function PublicRoute( {
    children
} : PublicRouteProps) {
    const {isAuthenticated} = useAuth()

    if (isAuthenticated) {
        return <Navigate to="/dashboard"/>
    }

    return children
}

export default PublicRoute; 
import { useEffect, useState } from "react";
import { getCurrentUser } from "../api/auth";
import { useNavigate } from "react-router-dom";
import { useAuth } from "../context/AuthContext";


function Dashboard() {
    const navigate = useNavigate()
    const { logout } = useAuth();

    const [user, setUser] = useState<any>(null)
    const [message, setMessage] = useState("")

    const handleLogout = () => {
        logout()
        navigate("/login")
    }

    useEffect(() => {
        const fetchUser = async () => {
            try {
                const response = await getCurrentUser();

                setUser(response)
            } catch (error) {
                console.log(`Exception: Failed to load user -- ${error}`)
                setMessage("Failed to load user.")
            }
        }

        fetchUser()
    }, [])

    return (
        <div className="
            min-h-screen
            flex
            flex-col
            items-center
            justify-center
            bg-gray-50
        ">

            <h1 className="
                text-4xl
                font-bold
                mb-6
            ">
                Dashboard
            </h1>

            {
                user && (

                    <div className="
                        bg-white
                        shadow-lg
                        rounded-2xl
                        p-8
                        w-full
                        max-w-md
                    ">

                        <p>
                            <strong>ID:</strong>
                            {" "}
                            {user.id}
                        </p>

                        <p>
                            <strong>Username:</strong>
                            {" "}
                            {user.username}
                        </p>

                        <p>
                            <strong>Email:</strong>
                            {" "}
                            {user.email}
                        </p>

                    </div>
                )
            }

            <button onClick={handleLogout}
                    className="
                        mt-6
                        bg-red-500
                        hover:gr-red-600
                        text-white
                        px-6
                        py-3
                        rounded-xl
                        font-semibold
                        transition
            " >  
                Logout
            </button>

            {
                message && (

                    <p className="
                        mt-5
                        text-red-500
                    ">
                        {message}
                    </p>
                )
            }

        </div>
    );
}

export default Dashboard;

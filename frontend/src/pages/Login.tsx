import { useState } from "react";
import { useNavigate } from "react-router-dom"
import { useAuth } from "../context/AuthContext";

import AuthLayout from "../layouts/AuthLayout";

import { loginUser } from "../api/auth";
import { Link } from "react-router-dom";

function Login() {
    const navigate = useNavigate()
    const { login } = useAuth();
    
    const [email, setEmail] = useState("");

    const [password, setPassword] = useState("");

    const [message, setMessage] = useState("");

    const handleLogin = async (
        event: any
    ) => {

        event.preventDefault();

        try {

            const response = await loginUser(
                email,
                password
            );
            
            login(response.access_token)

            navigate("/dashboard");

        } catch (error: any) {

            setMessage(
                error.response?.data?.detail ||
                "Login failed."
            );
        }
    };

    return (
        
        <AuthLayout>

            <div className="flex flex-col items-center mb-8">

                <div className="
                    w-14
                    h-14
                    rounded-xl
                    bg-indigo-600
                    flex
                    items-center
                    justify-center
                    mb-4
                ">

                    <span className="
                        text-white
                        text-2xl
                        font-bold
                    ">
                        D
                    </span>

                </div>

                <h1 className="
                    text-3xl
                    font-bold
                    text-gray-900
                ">
                    Welcome back!
                </h1>

                <p className="
                    text-gray-500
                    mt-2
                    text-center
                ">
                    Sign in to your account
                </p>

            </div>

            <form
                onSubmit={handleLogin}
                className="space-y-4"
            >

                <div>

                    <label className="
                        text-sm
                        font-medium
                        text-gray-700
                    ">
                        Email
                    </label>

                    <input
                        type="email"
                        placeholder="john@example.com"
                        value={email}
                        onChange={(e) =>
                            setEmail(e.target.value)
                        }
                        className={inputClass}
                    />

                </div>

                <div>

                    <label className="
                        text-sm
                        font-medium
                        text-gray-700
                    ">
                        Password
                    </label>

                    <input
                        type="password"
                        placeholder="Password"
                        value={password}
                        onChange={(e) =>
                            setPassword(e.target.value)
                        }
                        className={inputClass}
                    />

                </div>

                <button
                    type="submit"
                    className="
                        w-full
                        bg-indigo-600
                        hover:bg-indigo-700
                        text-white
                        py-3
                        rounded-xl
                        font-semibold
                        transition
                    "
                >
                    Sign in
                </button>

            </form>
            
            <p className="
                mt-6
                text-center
                text-sm
                text-gray-500
            ">

                Don't have an account?

                <Link
                    to="/register"
                    className="
                        ml-1
                        text-indigo-600
                        hover:text-indigo-700
                        font-medium
                    "
                >
                    Register
                </Link>

            </p>

            {
                message && (
                    <p className="
                        mt-5
                        text-center
                        text-indigo-600
                    ">
                        {message}
                    </p>
                )
            }

        </AuthLayout>
    );
}


const inputClass = `
    w-full
    px-4
    py-3
    border
    border-gray-300
    rounded-xl
    focus:outline-none
    focus:ring-2
    focus:ring-indigo-500
`;

export default Login;
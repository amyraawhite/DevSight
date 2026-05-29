import { useState } from "react";
import { registerUser } from "../api/auth";
import AuthLayout from "../layouts/AuthLayout";
import { Link } from "react-router-dom";


function Register() {
    // State
    const [username, setUsername] = useState("")
    const [email, setEmail] = useState("")
    const [password, setPassword] = useState("")
    const [fullName, setFullName] = useState("");
    const [confirmPassword, setConfirmPassword] = useState("");

    const [message, setMessage] = useState("")

    const handleRegister = async (
        event : any
    ) => {
        event.preventDefault()
        if (password !== confirmPassword) {
            setMessage("Passwords do not match.");

            return;
        }
        try {
            const response = await registerUser(
                username, 
                email,
                password
            )

            setMessage(response.message)
            
        } catch (error : any) {
            setMessage(error.response?.data?.detail || "Registration Failed.")
        }
    }

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
                    Create your account
                </h1>

                <p className="
                    text-gray-500
                    mt-2
                    text-center
                ">
                    Get started with DevSight
                </p>

            </div>

            <form
                onSubmit={handleRegister}
                className="space-y-4"
            >
                
                <label className="text-sm font-medium text-gray-900">Full Name</label>
                <input
                    type="text"
                    placeholder="Full Name"
                    value={fullName}
                    onChange={(e) =>
                        setFullName(e.target.value)
                    }
                    className={inputClass}
                />

                <label className="text-sm font-medium text-gray-900">Username</label>
                <input
                    type="text"
                    placeholder="Username"
                    value={username}
                    onChange={(e) =>
                        setUsername(e.target.value)
                    }
                    className={inputClass}
                />

                <label className="text-sm font-medium text-gray-900">Email</label>
                <input
                    type="email"
                    placeholder="Email"
                    value={email}
                    onChange={(e) =>
                        setEmail(e.target.value)
                    }
                    className={inputClass}
                />

                <label className="text-sm font-medium text-gray-900">Password</label>
                <input
                    type="password"
                    placeholder="Password"
                    value={password}
                    onChange={(e) =>
                        setPassword(e.target.value)
                    }
                    className={inputClass}
                />

                <label className="text-sm font-medium text-gray-900">Confirm Password</label>
                <input
                    type="password"
                    placeholder="Confirm Password"
                    value={confirmPassword}
                    onChange={(e) =>
                        setConfirmPassword(e.target.value)
                    }
                    className={inputClass}
                />

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
                    Create account
                </button>

            </form>

            <p className="
                mt-6
                text-center
                text-sm
                text-gray-500
            ">

                Already have an account?

                <Link
                    to="/login"
                    className="
                        ml-1
                        text-indigo-600
                        hover:text-indigo-700
                        font-medium
                    "
                >
                    Sign in
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

export default Register;
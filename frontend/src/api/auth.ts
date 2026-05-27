import axios from "axios"; 

const API_URL="http://localhost:8000";

// =========================
// Register User
// =========================
export const registerUser = async (
    username : string,
    email : string,
    password : string,
) => {
    const response = await axios.post(
        `${API_URL}/auth/register`,
        {
            username, 
            email,
            password
        }
    );

    return response.data;
}


// =========================
// Login User
// =========================
export const loginUser = async (
    email : string,
    password : string,
) => {
    const formData = new URLSearchParams();

    formData.append("username", email)
    formData.append("password", password)

    const response = await axios.post(
        `${API_URL}/auth/login`,
        formData,
        {
            headers : {
                "Content-Type":
                    "application/x-www-form-urlencoded"
            }
        }
    );

    return response.data;
}
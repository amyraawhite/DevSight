import { Outlet, NavLink, useNavigate } from "react-router-dom"; 
import { useAuth } from "../context/AuthContext";


function AppLayout() {
    const navigate = useNavigate()

    const { logout } = useAuth()

    const handleLogout = () => {
        logout()
        navigate("/login")
    }

    return (
        <div className="
            h-screen
            overflow-hidden
            flex
            bg-[#F5F7FB]
        ">
            {/*===================
                Sidebar
            ====================*/}
            <aside className="
                w-72
                shrink-0
                bg-[#0B1120]
                text-white
                flex
                flex-col
                justify-between
                px-6
                py-8
                shawdown-2xl
                
            ">
                <div>
                    {/* Logo */}
                    <div className="
                        flex
                        items-center
                        gap-3
                        mb-12
                    ">
                        <div className="
                            w-12
                            h-12
                            rounded-2xl
                            bg-indigo-600
                            flex
                            items-center
                            justify-center
                            text-2xl
                            font-bold
                        ">
                            D
                        </div>

                        <div>
                            <h1 className="
                                text-2xl
                                font-bold
                            ">
                                DevSight
                            </h1>
                        </div>
                    </div>

                    <nav className="
                        flex
                        flex-col
                        gap-3
                    ">
                        <NavLink 
                            to="/dashboard"
                            className={({ isActive }) => `
                                px-4
                                py-3
                                rounded-xl
                                transition
                                font-medium

                                ${isActive
                                    ? "bg-indigo-600 text-white"
                                    : "hover:bg-white/10 text-gray-300"
                                }
                            `}
                        > 
                            Dashboard
                        </NavLink>

                         <NavLink
                            to="/projects"
                            className={({ isActive }) => `
                                px-4
                                py-3
                                rounded-xl
                                transition
                                font-medium

                                ${isActive
                                    ? "bg-indigo-600 text-white"
                                    : "hover:bg-white/10 text-gray-300"
                                }
                            `}
                        >
                            Projects
                        </NavLink>

                        <NavLink
                            to="/scans"
                            className={({ isActive }) => `
                                px-4
                                py-3
                                rounded-xl
                                transition
                                font-medium

                                ${isActive
                                    ? "bg-indigo-600 text-white"
                                    : "hover:bg-white/10 text-gray-300"
                                }
                            `}
                        >
                            Scans
                        </NavLink>

                        <NavLink
                            to="/reports"
                            className={({ isActive }) => `
                                px-4
                                py-3
                                rounded-xl
                                transition
                                font-medium

                                ${isActive
                                    ? "bg-indigo-600 text-white"
                                    : "hover:bg-white/10 text-gray-300"
                                }
                            `}
                        >
                            Reports
                        </NavLink>
                    </nav>
                </div>

                 {/* Bottom User Section */}
                <div className="
                    border-t
                    border-white/10
                    pt-6
                ">

                    <button
                        onClick={handleLogout}
                        className="
                            w-full
                            bg-red-500
                            hover:bg-red-600
                            text-white
                            py-3
                            rounded-xl
                            font-semibold
                            transition
                        "
                    >
                        Logout
                    </button>

                </div>

            </aside>

            {/* =========================
                Main Content
            ========================= */}
            <div className="
                flex-1
                flex
                flex-col
                overflow-hidden
            ">

                {/* Navbar */}
                <header className="
                    h-24
                    shrink-0
                    bg-white
                    border-b
                    border-gray-200
                    px-10
                    flex
                    items-center
                    justify-between
                ">

                    {/* Search */}
                    <div className="
                        w-full
                        max-w-xl
                    ">

                        <input
                            type="text"
                            placeholder="Search..."
                            className="
                                w-full
                                px-5
                                py-3
                                rounded-2xl
                                border
                                border-gray-300
                                focus:outline-none
                                focus:ring-2
                                focus:ring-indigo-500
                            "
                        />

                    </div>

                    {/* Right Section */}
                    <div className="
                        flex
                        items-center
                        gap-5
                        ml-6
                    ">

                        {/* Notification */}
                        <button className="
                            w-12
                            h-12
                            rounded-full
                            bg-gray-100
                            hover:bg-gray-200
                            transition
                        ">
                            🔔
                        </button>

                        {/* Avatar */}
                        <div className="
                            w-12
                            h-12
                            rounded-full
                            bg-indigo-600
                            flex
                            items-center
                            justify-center
                            text-white
                            font-bold
                        ">
                            A
                        </div>

                    </div>

                </header>

                {/* Routed Content */}
                <main className="
                    flex-1
                    overflow-y-auto
                    p-10
                ">

                    <Outlet />

                </main>

            </div>
        </div>
    )
}

export default AppLayout;
import type { ReactNode } from "react";

type AuthLayoutProps = {
    children: ReactNode;
};

function AuthLayout({
    children
}: AuthLayoutProps) {

    return (

        <div className="
            min-h-screen
            flex
            items-center
            justify-center
            bg-gray-50
            px-6
            relative
            overflow-hidden
        ">

            {/* Background Glow */}
            <div className="
                absolute
                bottom-[-150px]
                right-[-100px]
                w-[500px]
                h-[500px]
                bg-gradient-to-tr
                from-indigo-300
                via-purple-200
                to-blue-200
                rounded-full
                blur-3xl
                opacity-60
            " />

            {/* Auth Card */}
            <div className="
                relative
                z-10
                w-full
                max-w-md
                bg-white
                rounded-3xl
                shadow-xl
                p-10
            ">

                {children}

            </div>

        </div>
    );
}

export default AuthLayout;
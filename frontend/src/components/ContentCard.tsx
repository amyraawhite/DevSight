type ContentCardProps = {
    title : string;
    children : React.ReactNode;
}

function ContentCard({
    title,
    children
} : ContentCardProps) {
        return (
            <div className="
                bg-white
                rounded-2xl
                shadow-sm
                border
                border-gray-100
                p-6
            ">

                <div className="
                    mb-6
                ">

                    <h2 className="
                        text-xl
                        font-bold
                        text-gray-900
                    ">
                        {title}
                    </h2>

                </div>

                {children}

            </div>
    );

}

export default ContentCard;
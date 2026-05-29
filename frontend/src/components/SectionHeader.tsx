type SectionHeaderProps = {

    title: string;

    subtitle?: string;
};

function SectionHeader({

    title,
    subtitle

}: SectionHeaderProps) {

    return (

        <div className="mb-10">

            <h1 className="
                text-4xl
                font-bold
                text-gray-900
            ">
                {title}
            </h1>

            {
                subtitle && (

                    <p className="
                        text-gray-500
                        mt-2
                    ">
                        {subtitle}
                    </p>
                )
            }

        </div>
    );
}

export default SectionHeader;
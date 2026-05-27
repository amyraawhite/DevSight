type StatCardProps = {
    title : string; 
    value : string;
    subtitle? : string;

    trend? : string;
    trendColor? : string;

    icon ?: string;
    iconBackground? : string;
}

function StatCard({
    title,
    value,
    subtitle,
    trend,
    trendColor = "text-green-500",
    icon = "📊",
    iconBackground = "bg-indigo-100"
}: StatCardProps) {
    return (

        <div className="
            bg-white
            rounded-3xl
            border
            border-gray-100
            shadow-sm
            p-6
            flex
            justify-between
            items-start
        ">

            <div>

                <p className="
                    text-gray-500
                    text-sm
                    font-medium
                ">
                    {title}
                </p>

                <h2 className="
                    text-5xl
                    font-bold
                    text-gray-900
                    mt-4
                ">
                    {value}
                </h2>

                {
                    trend && (

                        <p className={`
                            mt-4
                            text-sm
                            font-semibold
                            ${trendColor}
                        `}>
                            {trend}
                        </p>
                    )
                }

                {
                    subtitle && (

                        <p className="
                            text-gray-400
                            text-sm
                            mt-1
                        ">
                            {subtitle}
                        </p>
                    )
                }

            </div>

            {/* Icon */}
            <div className={`
                w-16
                h-16
                rounded-2xl
                flex
                items-center
                justify-center
                text-3xl
                ${iconBackground}
            `}>

                {icon}

            </div>

        </div>
    );
}

export default StatCard;
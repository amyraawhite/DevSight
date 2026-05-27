import { useEffect, useState } from "react";
import { getCurrentUser } from "../api/auth";

import StatCard from "../components/StatCard";
import ContentCard from "../components/ContentCard";
import SectionHeader from "../components/SectionHeader";

function Dashboard() {
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
        <div>

            <SectionHeader
                title="Welcome back, Amyra! 👋"
                subtitle="Here's what's happening with your projects today."
            />

            {/* Example Cards */}
            <div className="
                grid
                grid-cols-1
                md:grid-cols-2
                xl:grid-cols-4
                gap-6
            ">

                <StatCard
                    title="Projects"
                    value="6"
                    trend="+1 this week"
                    trendColor="text-green-500"
                    icon="📚"
                    iconBackground="bg-indigo-100"
                />

                <StatCard
                    title="Open Alerts"
                    value="12"
                    trend="+3 this week"
                    trendColor="text-red-500"
                    icon="🛡️"
                    iconBackground="bg-red-100"
                />

                <StatCard
                    title="Security Score"
                    value="78"
                    trend="+6 this week"
                    trendColor="text-green-500"
                    icon="✅"
                    iconBackground="bg-green-100"
                />

                <StatCard
                    title="Tasks"
                    value="24"
                    trend="+5 this week"
                    trendColor="text-blue-500"
                    icon="📋"
                    iconBackground="bg-blue-100"
                />

            </div>

            <div className="
                grid
                grid-cols-1
                xl:grid-cols-3
                gap-6
                mt-8
            ">

                {/* =========================
                    Security Trend
                ========================= */}
                <div className="xl:col-span-2">

                    <ContentCard title="Security Trend">

                        <div className="
                            h-80
                            flex
                            flex-col
                            justify-between
                        ">

                            {/* Fake Chart Area */}
                            <div className="
                                flex-1
                                flex
                                items-end
                                gap-4
                                pt-10
                            ">

                                <div className="
                                    w-full
                                    bg-indigo-200
                                    rounded-t-xl
                                    h-24
                                " />

                                <div className="
                                    w-full
                                    bg-indigo-300
                                    rounded-t-xl
                                    h-40
                                " />

                                <div className="
                                    w-full
                                    bg-indigo-400
                                    rounded-t-xl
                                    h-32
                                " />

                                <div className="
                                    w-full
                                    bg-indigo-500
                                    rounded-t-xl
                                    h-52
                                " />

                                <div className="
                                    w-full
                                    bg-indigo-600
                                    rounded-t-xl
                                    h-64
                                " />

                                <div className="
                                    w-full
                                    bg-indigo-500
                                    rounded-t-xl
                                    h-56
                                " />

                                <div className="
                                    w-full
                                    bg-indigo-700
                                    rounded-t-xl
                                    h-72
                                " />

                            </div>

                            {/* Bottom Labels */}
                            <div className="
                                flex
                                justify-between
                                text-sm
                                text-gray-400
                                mt-6
                            ">

                                <span>Mon</span>
                                <span>Tue</span>
                                <span>Wed</span>
                                <span>Thu</span>
                                <span>Fri</span>
                                <span>Sat</span>
                                <span>Sun</span>

                            </div>

                        </div>

                    </ContentCard>

                </div>

                {/* =========================
                    Severity Breakdown
                ========================= */}
                <ContentCard title="Alerts by Severity">

                    <div className="
                        flex
                        flex-col
                        items-center
                        justify-center
                        h-full
                        gap-8
                        py-6
                    ">

                        {/* Circle */}
                        <div className="
                            w-52
                            h-52
                            rounded-full
                            border-[22px]
                            border-red-400
                            relative
                            flex
                            items-center
                            justify-center
                        ">

                            <div className="
                                text-center
                            ">

                                <h2 className="
                                    text-5xl
                                    font-bold
                                ">
                                    12
                                </h2>

                                <p className="
                                    text-gray-400
                                    mt-1
                                ">
                                    Total
                                </p>

                            </div>

                        </div>

                        {/* Legend */}
                        <div className="
                            w-full
                            flex
                            flex-col
                            gap-4
                        ">

                            <div className="
                                flex
                                justify-between
                                items-center
                            ">

                                <div className="
                                    flex
                                    items-center
                                    gap-3
                                ">

                                    <div className="
                                        w-4
                                        h-4
                                        rounded-full
                                        bg-red-500
                                    " />

                                    <span>Critical</span>

                                </div>

                                <span className="
                                    text-gray-500
                                ">
                                    3
                                </span>

                            </div>

                            <div className="
                                flex
                                justify-between
                                items-center
                            ">

                                <div className="
                                    flex
                                    items-center
                                    gap-3
                                ">

                                    <div className="
                                        w-4
                                        h-4
                                        rounded-full
                                        bg-yellow-500
                                    " />

                                    <span>Medium</span>

                                </div>

                                <span className="
                                    text-gray-500
                                ">
                                    5
                                </span>

                            </div>

                            <div className="
                                flex
                                justify-between
                                items-center
                            ">

                                <div className="
                                    flex
                                    items-center
                                    gap-3
                                ">

                                    <div className="
                                        w-4
                                        h-4
                                        rounded-full
                                        bg-green-500
                                    " />

                                    <span>Low</span>

                                </div>

                                <span className="
                                    text-gray-500
                                ">
                                    4
                                </span>

                            </div>

                        </div>

                    </div>

                </ContentCard>

            </div>

            <div className="
                grid
                grid-cols-1
                xl:grid-cols-2
                gap-6
                mt-8
            ">

                {/* =========================
                    Recent Alerts
                ========================= */}
                <ContentCard title="Recent Alerts">

                    <div className="
                        flex
                        flex-col
                        divide-y
                        divide-gray-100
                    ">

                        {/* Alert Item */}
                        <div className="
                            py-4
                            flex
                            justify-between
                            items-start
                        ">

                            <div>

                                <div className="
                                    flex
                                    items-center
                                    gap-3
                                    mb-2
                                ">

                                    <span className="
                                        px-3
                                        py-1
                                        rounded-full
                                        bg-red-100
                                        text-red-600
                                        text-xs
                                        font-semibold
                                    ">
                                        Critical
                                    </span>

                                </div>

                                <h3 className="
                                    font-semibold
                                    text-gray-900
                                ">
                                    SQL Injection detected
                                </h3>

                                <p className="
                                    text-sm
                                    text-gray-400
                                    mt-1
                                ">
                                    auth-service • May 25, 2026
                                </p>

                            </div>

                            <span className="
                                text-sm
                                text-gray-400
                            ">
                                10:21 AM
                            </span>

                        </div>

                        {/* Alert Item */}
                        <div className="
                            py-4
                            flex
                            justify-between
                            items-start
                        ">

                            <div>

                                <div className="
                                    flex
                                    items-center
                                    gap-3
                                    mb-2
                                ">

                                    <span className="
                                        px-3
                                        py-1
                                        rounded-full
                                        bg-yellow-100
                                        text-yellow-700
                                        text-xs
                                        font-semibold
                                    ">
                                        High
                                    </span>

                                </div>

                                <h3 className="
                                    font-semibold
                                    text-gray-900
                                ">
                                    Exposed AWS Access Key
                                </h3>

                                <p className="
                                    text-sm
                                    text-gray-400
                                    mt-1
                                ">
                                    api-gateway • May 25, 2026
                                </p>

                            </div>

                            <span className="
                                text-sm
                                text-gray-400
                            ">
                                9:15 AM
                            </span>

                        </div>

                        {/* Alert Item */}
                        <div className="
                            py-4
                            flex
                            justify-between
                            items-start
                        ">

                            <div>

                                <div className="
                                    flex
                                    items-center
                                    gap-3
                                    mb-2
                                ">

                                    <span className="
                                        px-3
                                        py-1
                                        rounded-full
                                        bg-orange-100
                                        text-orange-700
                                        text-xs
                                        font-semibold
                                    ">
                                        Medium
                                    </span>

                                </div>

                                <h3 className="
                                    font-semibold
                                    text-gray-900
                                ">
                                    Outdated dependency: lodash
                                </h3>

                                <p className="
                                    text-sm
                                    text-gray-400
                                    mt-1
                                ">
                                    frontend-web • May 24, 2026
                                </p>

                            </div>

                            <span className="
                                text-sm
                                text-gray-400
                            ">
                                4:33 PM
                            </span>

                        </div>

                    </div>

                </ContentCard>

                {/* =========================
                    Recent Activity
                ========================= */}
                <ContentCard title="Recent Activity">

                    <div className="
                        flex
                        flex-col
                        divide-y
                        divide-gray-100
                    ">

                        <div className="
                            py-4
                            flex
                            justify-between
                            items-center
                        ">

                            <div className="
                                flex
                                items-center
                                gap-4
                            ">

                                <div className="
                                    w-10
                                    h-10
                                    rounded-full
                                    bg-indigo-100
                                    flex
                                    items-center
                                    justify-center
                                ">
                                    🛡️
                                </div>

                                <div>

                                    <h3 className="
                                        font-medium
                                        text-gray-900
                                    ">
                                        New alert in auth-service
                                    </h3>

                                </div>

                            </div>

                            <span className="
                                text-sm
                                text-gray-400
                            ">
                                10:21 AM
                            </span>

                        </div>

                        <div className="
                            py-4
                            flex
                            justify-between
                            items-center
                        ">

                            <div className="
                                flex
                                items-center
                                gap-4
                            ">

                                <div className="
                                    w-10
                                    h-10
                                    rounded-full
                                    bg-green-100
                                    flex
                                    items-center
                                    justify-center
                                ">
                                    ✅
                                </div>

                                <div>

                                    <h3 className="
                                        font-medium
                                        text-gray-900
                                    ">
                                        Security scan completed
                                    </h3>

                                </div>

                            </div>

                            <span className="
                                text-sm
                                text-gray-400
                            ">
                                9:15 AM
                            </span>

                        </div>

                        <div className="
                            py-4
                            flex
                            justify-between
                            items-center
                        ">

                            <div className="
                                flex
                                items-center
                                gap-4
                            ">

                                <div className="
                                    w-10
                                    h-10
                                    rounded-full
                                    bg-blue-100
                                    flex
                                    items-center
                                    justify-center
                                ">
                                    👤
                                </div>

                                <div>

                                    <h3 className="
                                        font-medium
                                        text-gray-900
                                    ">
                                        New user added
                                    </h3>

                                </div>

                            </div>

                            <span className="
                                text-sm
                                text-gray-400
                            ">
                                Yesterday
                            </span>

                        </div>

                    </div>

                </ContentCard>

            </div>

        </div>
    );
}

export default Dashboard;

import asyncio

from linkedin.linkedin_connect import LinkedInConnect


async def main() -> int:
    linkedin_connect: LinkedInConnect = LinkedInConnect()

    try:

        await linkedin_connect.execute_linkedin_connection()
        return 0

    except Exception as e:
        raise e


if __name__ == "__main__":
    asyncio.run(main())

import styles from "./page.module.css";
import Link from "next/link";
import { useRouter } from "next/navigation";

export default function Home() {
  return (
    <main className={styles.main}>
      <div className={styles.center}>
        <h1>Gist</h1>
        <p>Gist summarizes data in a fun and amusing manner</p>
      </div>

      <div className={styles.grid}>
        <Link
          href="https://nextjs.org/docs?utm_source=create-next-app&utm_medium=appdir-template&utm_campaign=create-next-app"
          className={styles.card}
        >
          <h2>
            Login <span>-&gt;</span>
          </h2>
        </Link>

        <Link
          href="https://nextjs.org/learn?utm_source=create-next-app&utm_medium=appdir-template&utm_campaign=create-next-app"
          className={styles.card}
        >
          <h2>
            About Us <span>-&gt;</span>
          </h2>
        </Link>

        <Link href="/demo" className={styles.card}>
          <h2>
            Demo <span>-&gt;</span>
          </h2>
        </Link>
      </div>
    </main>
  );
}

"use client";
import styles from "../page.module.css";
import { useEffect, useState } from "react";

export default function Demo() {
  const [body, setBody] = useState("");
  const [images, setImages] = useState<string[]>([]);
  const [subject, setSubject] = useState<string[]>([]);
  const [summary, setSummary] = useState([]);
  const [sender, setSender] = useState([]);

  useEffect(() => {
    fetch("http://localhost:8000/data")
      .then((response) => response.json())
      .then((data) => {
        const img = [];
        const subjects = [];
        const bodies = [];
        const senders = [];
        const summaries = [];
        data.forEach((dt) => {
          img.push({
            src: dt.image_url,
            alt: "",
            caption: "Image!!",
          });
          subjects.push(dt.subject);
          bodies.push(dt.body);
          senders.push(dt.sender);
          summaries.push(dt.summary);
        });
        setImages(img);
        setSubject(subjects);
        setBody(bodies);
        setSender(senders);
        setSummary(summaries);
      });
  }, []);

  return (
    <main className={styles.main}>
      <div className={styles.centerImages}>
        {images.map((image, index) => (
          <>
            <div>Subject: {subject[index]}</div>
            <div>
              <p>Summary: {summary[index]}</p>
            </div>
            <div className={styles.flipCard}>
              <div className={styles.flipCardInner}>
                <div className={styles.flipCardFront}>
                  <img
                    key={index}
                    src={image.src}
                    alt={image.alt}
                    height={200}
                    width={200}
                  />
                </div>
                <div className={styles.flipCardBack}>
                  <p>{sender[index]}</p>
                  <p style={{ marginTop: "10px" }}>{body[index]}</p>
                </div>
              </div>
            </div>
          </>
        ))}
      </div>
    </main>
  );
}

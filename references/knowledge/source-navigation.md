# Source navigation and retrieval

Use this map for English requests against Hindi/Hinglish originals. Choose topic → source map → exact extract. All nine originals remain authoritative. Chunking is lossless over the full timestamped transcript body and includes long T09 utterances. Read preceding/following extracts when a thought crosses a boundary. Chunk presence is not proof that every statement has been independently fact-checked.

## Module maps

For exact citation verification with a Python runtime, run `python scripts/read_source.py --source T08 --timestamp 04:35 --context 1` from the skill folder. Add `--quote "specific, relatable hook"` to check a verbatim excerpt. It checks original bytes and rejects missing timestamps or mismatched quotes; it does not substitute a nearby passage. Context includes adjacent original utterances, not a summary. If code execution is unavailable, read the original passage and its neighbours directly. Retrieval verifies provenance, not whether an interpretation follows from the quote.

- [T01: 01 - Ad Creative Essentials and Psychology.txt](T01-source-map.md)

- [T02: 02 - Ad Angles and UGC Strategies.txt](T02-source-map.md)

- [T03: 03 - Value-Based Advertising Strategies.txt](T03-source-map.md)

- [T04: 04 - Creating High-Converting Statistics Ads.txt](T04-source-map.md)

- [T05: 05 - Street Interview Ad Strategies.txt](T05-source-map.md)

- [T06: 06 - Low Budget Content Creation.txt](T06-source-map.md)

- [T07: 07 - Ad Script Writing Frameworks.txt](T07-source-map.md)

- [T08: 08 - Improving Ad Scripts.txt](T08-source-map.md)

- [T09: 09 - Mini Vlog Ad Strategy.txt](T09-source-map.md)

## Topic routes

| English intent | Primary source maps | Search terms in the original |

|---|---|---|

| audience and awareness | [T01](T01-source-map.md), [T02](T02-source-map.md), [T03](T03-source-map.md) | ऑडियंस, अवेयर, audience, aware |

| psychology and desire | [T01](T01-source-map.md), [T03](T03-source-map.md) | साइकोलॉजी, डिज़ायर, प्लेज़र, psychology, dream |

| hooks and attention | [T01](T01-source-map.md), [T07](T07-source-map.md), [T08](T08-source-map.md) | हुक, hook, अटेंशन |

| body and credibility | [T01](T01-source-map.md), [T07](T07-source-map.md) | बॉडी, क्रेडिबिलिटी, credibility |

| CTA and single action | [T01](T01-source-map.md), [T07](T07-source-map.md), [T08](T08-source-map.md) | सीटीए, CTA, एक्शन |

| angle expansion and objections | [T02](T02-source-map.md) | एंगल, angle, ऑब्जेक्शन, objection |

| UGC | [T02](T02-source-map.md) | यूजीसी, UGC |

| value stack | [T03](T03-source-map.md) | value, स्टैक, वैल्यू |

| meme | [T03](T03-source-map.md) | meme, मीम, मेम |

| educational | [T03](T03-source-map.md) | educational, एजुकेशनल |

| comparison us versus them | [T03](T03-source-map.md) | कंपैरिजन, comparison, वर्सेस डेम |

| before and after | [T03](T03-source-map.md) | बिफोर, before, आफ्टर |

| statistics and evidence | [T04](T04-source-map.md) | statistic, स्टैटिस्टिक, सोर्स, source |

| ugly ads | [T04](T04-source-map.md) | ugly, अग्ली, अनपॉलिश |

| founder ads | [T04](T04-source-map.md) | founder, फाउंडर |

| testimonial | [T04](T04-source-map.md) | testimonial, टेस्टिमोनियल |

| podcast | [T04](T04-source-map.md) | podcast, पॉडकास्ट |

| street interview | [T05](T05-source-map.md) | street, स्ट्रीट, इंटरव्यू |

| mini drama | [T05](T05-source-map.md) | drama, ड्रामा |

| calling out | [T05](T05-source-map.md) | calling, कॉलिंग, call out |

| first person POV | [T05](T05-source-map.md) | POV, पीओवी, पॉइंट ऑफ व्यू |

| office and warehouse | [T05](T05-source-map.md) | office, ऑफिस, warehouse, वेयरहाउस |

| ad review | [T05](T05-source-map.md) | review, रिव्यू |

| AMA | [T05](T05-source-map.md) | AMA, आस्क, स्टिकर |

| storytelling | [T05](T05-source-map.md) | story, स्टोरी |

| low budget lighting audio | [T06](T06-source-map.md) | लाइट, light, माइक्रोफोन, audio, बैकग्राउंड |

| HPSCPC and script frameworks | [T07](T07-source-map.md) | हुक, क्रेडिबिलिटी, framework, फ्रेमवर्क |

| script critique and diversity | [T08](T08-source-map.md) | specific, स्पेसिफिक, format, फॉर्मेट, same |

| mini vlog | [T09](T09-source-map.md) | व्लॉग, vlog |

| screen recording | [T09](T09-source-map.md) | स्क्रीन, screen |

| AI concept and product consistency | [T09](T09-source-map.md) | एआई, AI, कंसिस्ट, कॉन्सेप्ट, concept |

| advanced production | [T09](T09-source-map.md) | ISO, आईएसओ, लाइटिंग, शटर, shutter |

## Answer procedure

1. Identify the requested decision, business, audience, deliverable and language. Read only relevant source modules, not the entire corpus by default.

2. Find the exact passage. The working digest is a route, never the sole evidence for detailed training claims. If local Python is available, scripts/search_transcripts.py supports optional offline keyword lookup; it is not a required runtime.

3. Verify the original sentence and surrounding context. Translate its meaning faithfully. Record source ID, exact timestamp and claim category. Do not fabricate timestamp precision.

4. Apply the principle to verified client facts. Use a small number of directly relevant principles rather than a generic inventory of frameworks.

5. Distinguish source-backed rules, business facts and proposed hypotheses. If evidence is missing, state the narrow gap and use placeholders rather than assertions.

6. Run accuracy-and-relevance.md. Cite the supporting source/timestamp succinctly. Never claim that merely embedding files guarantees perfect accuracy.


## Supplemental measurement source
[P01 metrics PDF notes](metrics-freebee-notes.md): reach/impressions (p1), CTR/CPC/conversion rate (p2), CPA/ROAS/engagement (p3), frequency/quality ranking/CPM (p4), attribution model performance (p5). The filename says 5 metrics; the document contains 12 topics. The nine original transcripts remain primary creative knowledge.

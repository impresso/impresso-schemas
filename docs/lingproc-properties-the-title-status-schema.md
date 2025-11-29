## title\_status Type

`object` ([The Title Status Schema](lingproc-properties-the-title-status-schema.md))

# title\_status Properties

| Property                        | Type      | Required | Nullable       | Defined by                                                                                                                                                                                                                       |
| :------------------------------ | :-------- | :------- | :------------- | :------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [exact\_prefix](#exact_prefix)  | `boolean` | Optional | cannot be null | [Untitled schema](lingproc-properties-the-title-status-schema-properties-exact_prefix.md "https://impresso.github.io/impresso-schemas/json/newspaper/ling_spacy.schema.json#/properties/title_status/properties/exact_prefix")   |
| [ellipsis](#ellipsis)           | `boolean` | Optional | cannot be null | [Untitled schema](lingproc-properties-the-title-status-schema-properties-ellipsis.md "https://impresso.github.io/impresso-schemas/json/newspaper/ling_spacy.schema.json#/properties/title_status/properties/ellipsis")           |
| [alnum\_prefix](#alnum_prefix)  | `boolean` | Optional | cannot be null | [Untitled schema](lingproc-properties-the-title-status-schema-properties-alnum_prefix.md "https://impresso.github.io/impresso-schemas/json/newspaper/ling_spacy.schema.json#/properties/title_status/properties/alnum_prefix")   |
| [alnum\_infix](#alnum_infix)    | `boolean` | Optional | cannot be null | [Untitled schema](lingproc-properties-the-title-status-schema-properties-alnum_infix.md "https://impresso.github.io/impresso-schemas/json/newspaper/ling_spacy.schema.json#/properties/title_status/properties/alnum_infix")     |
| [unknown](#unknown)             | `boolean` | Optional | cannot be null | [Untitled schema](lingproc-properties-the-title-status-schema-properties-unknown.md "https://impresso.github.io/impresso-schemas/json/newspaper/ling_spacy.schema.json#/properties/title_status/properties/unknown")             |
| [title\_longer](#title_longer)  | `boolean` | Optional | cannot be null | [Untitled schema](lingproc-properties-the-title-status-schema-properties-title_longer.md "https://impresso.github.io/impresso-schemas/json/newspaper/ling_spacy.schema.json#/properties/title_status/properties/title_longer")   |
| [advertisement](#advertisement) | `boolean` | Optional | cannot be null | [Untitled schema](lingproc-properties-the-title-status-schema-properties-advertisement.md "https://impresso.github.io/impresso-schemas/json/newspaper/ling_spacy.schema.json#/properties/title_status/properties/advertisement") |

## exact\_prefix

True if title is an exact case-sensitive prefix of full text

`exact_prefix`

* is optional

* Type: `boolean`

* cannot be null

* defined in: [Untitled schema](lingproc-properties-the-title-status-schema-properties-exact_prefix.md "https://impresso.github.io/impresso-schemas/json/newspaper/ling_spacy.schema.json#/properties/title_status/properties/exact_prefix")

### exact\_prefix Type

`boolean`

## ellipsis

Is there an ellipsis added to the title (that cannot be found in the text)? ...

`ellipsis`

* is optional

* Type: `boolean`

* cannot be null

* defined in: [Untitled schema](lingproc-properties-the-title-status-schema-properties-ellipsis.md "https://impresso.github.io/impresso-schemas/json/newspaper/ling_spacy.schema.json#/properties/title_status/properties/ellipsis")

### ellipsis Type

`boolean`

## alnum\_prefix

When reducing title and full text to alphanumeric characters, is the title a prefix of the full text?

`alnum_prefix`

* is optional

* Type: `boolean`

* cannot be null

* defined in: [Untitled schema](lingproc-properties-the-title-status-schema-properties-alnum_prefix.md "https://impresso.github.io/impresso-schemas/json/newspaper/ling_spacy.schema.json#/properties/title_status/properties/alnum_prefix")

### alnum\_prefix Type

`boolean`

## alnum\_infix

When reducing title and full text to alphanumeric characters, is the title an infix of the full text? Sometimes the real title comes second (because of page numbers or secondary titles that come first)

`alnum_infix`

* is optional

* Type: `boolean`

* cannot be null

* defined in: [Untitled schema](lingproc-properties-the-title-status-schema-properties-alnum_infix.md "https://impresso.github.io/impresso-schemas/json/newspaper/ling_spacy.schema.json#/properties/title_status/properties/alnum_infix")

### alnum\_infix Type

`boolean`

## unknown

Is there an artificial title (UNKWNON, UNTITLED) that indicates that there is no title

`unknown`

* is optional

* Type: `boolean`

* cannot be null

* defined in: [Untitled schema](lingproc-properties-the-title-status-schema-properties-unknown.md "https://impresso.github.io/impresso-schemas/json/newspaper/ling_spacy.schema.json#/properties/title_status/properties/unknown")

### unknown Type

`boolean`

## title\_longer

True if title is longer than full text which indicates a weird problematic situation.

`title_longer`

* is optional

* Type: `boolean`

* cannot be null

* defined in: [Untitled schema](lingproc-properties-the-title-status-schema-properties-title_longer.md "https://impresso.github.io/impresso-schemas/json/newspaper/ling_spacy.schema.json#/properties/title_status/properties/title_longer")

### title\_longer Type

`boolean`

## advertisement

For some newspapers, advertisements have an artifical title consisting of a serial number of a an advertisement and the page. This is not a real title. Examples: Adv.7 Page 4,

`advertisement`

* is optional

* Type: `boolean`

* cannot be null

* defined in: [Untitled schema](lingproc-properties-the-title-status-schema-properties-advertisement.md "https://impresso.github.io/impresso-schemas/json/newspaper/ling_spacy.schema.json#/properties/title_status/properties/advertisement")

### advertisement Type

`boolean`

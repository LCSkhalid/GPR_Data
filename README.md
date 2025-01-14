# GPR_Data

## Dataset Description
The dataset consists of high-resolution Ground Penetrating Radar (GPR) data, specifically A-scan and B-scan profiles, obtained using antennas operating at 400 MHz and 200 MHz. This dataset contains 2239 images with its corresponding annotations for buried utilities, voids, and intact zones, acquired across various infrastructure projects in different cities and towns across Morocco between 2019 and 2024. Annotations were created using the online annotation tool [makesense.ai](https://www.makesense.ai/) for all the images in the dataset. The exported annotations are provided in both YOLO and VOC XML formats, making them compatible with various types of models. 

- Underground utilities 'Utility'
- Underground cavities 'Cavity'

## Download
The dataset can be downloaded [here](https://data.mendeley.com/datasets/ww7fd9t325/1).

## Data Acquisition

The data acquisition process utilized two distinct antennas, a 400 MHz and a 200 MHz, both from GSSI, configured manually and operated in survey wheel mode. The 400 MHz antenna was set to a range of 50 ns with a gain point of 5, employing vertical filters with a low-pass frequency of 800 MHz and a high-pass frequency of 100 MHz It recorded data with 512 samples per scan, and the permittivity values were adjusted based on the material being inspected. Similarly, the 200 MHz antenna was configured with a range of 150 ns and the same gain point of 5. It used vertical filters with a lower low-pass frequency of 400 MHz and a high-pass frequency of 30 MHz while maintaining 512 samples per scan. As with the 400 MHz antenna, the permittivity for the 200 MHz antenna depended on the type of material inspected.
## Visualizations

### images from the data with annotations:

![Screenshot](dataset.png)

## Data Processing

### Profiles Cropping
The original GPR profiles were cropped into `224×224` using the Python script `crop.py` to meet the preferred training size for performing transfer learning with different backbones such as `VGG19`.

### Data Augmentation
The created patches were augmented using the Python script `augmentation.py`, which includes various data augmentation techniques:
- Geometric transformations (random rotations, scaling, and flipping)
- Random noise
- Spectral shifting
- Elastic deformations
- Time-shifting

# Files Description

### Dataset Structure

- **`GPR_data` folder**: Contains 2,239 images, including:
  - 553 void images  
  - 786 underground utility images  
  - 900 intact images  
  - Cavities and utilities are accompanied by corresponding annotations in both YOLO and VOC XML formats.  
  - Includes original image files prior to the data augmentation step to ensure reproducibility.  
  - The dataset provides three distinct classes: voids, utilities, and intact areas, making it highly valuable for training machine learning models tailored to underground anomaly detection.

- **`augmented_cavities` folder**: Contains 553 cavity images and an annotation folder `annotations` with subfolders for two annotation formats:
  - **`VOC_XML_format` folder**: Contains 553 `.xml` files  
  - **`Yolo_format` folder**: Contains 553 `.txt` files  

- **`augmented_utilities` folder**: Contains 786 underground utility images and a corresponding annotation folder `annotations` with subfolders for two annotation formats:
  - **`VOC_XML_format` folder**: Contains 786 `.xml` files  
  - **`Yolo_format` folder**: Contains 786 `.txt` files  

- **`augmented_intact` folder**: Contains 900 intact images with no anomalies.

- **`cavities` folder**: Contains 79 original profiles with cavities.

- **`Utilities` folder**: Contains 131 original profiles with underground utilities.

- **`intact` folder**: Contains 75 original intact profiles.

Image filenames are defined with an ID number, such as:
 
 1_aug_7.JPG correspond to the first augmentation process on the first image.
 
# Citing the dataset

If you use this dataset, please cite the following publication:

_A. MOJAHID, D. EL OUAI, K. El Amraoui, K. EL-HAMI,  H. AITBENAMER, (2024).Intelligent Recognition of Subsurface Utilities and Voids: A Ground Penetrating Radar Dataset for Deep Learning Applications. in data in brief journal 10.17632/ww7fd9t325.1_ 


            @article{mojahid2024Intelligent,
            title={Intelligent Recognition of Subsurface Utilities and Voids: A Ground Penetrating Radar Dataset for Deep Learning Applications.},
            author={Abdelaziz MOJAHID, Driss EL OUAI, Khalid EL AMRAOUI, Khalil EL HAMI, Hamou AITBENAMER},
            journal={Data in Brief},
            pages={ },
            year={ },
            ISSN = { },
            doi = {10.17632/ww7fd9t325.1},
            publisher={Elsevier}
            }
            

            

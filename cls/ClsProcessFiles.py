import cls.ClsDBConn as db

# import components.create_db as db
import components.process_xml as xd
import components.insert_data as ind
import components.validate_data as vd
import components.common as cm


class ProcessFiles:

    @staticmethod
    def process(self, xmlFileNames):
        print('inside process files function')
        print(xmlFileNames)

        if len(xmlFileNames) > 0:
            for file in xmlFileNames:
                fileName = file[file.rindex("/") + 1:]
                dbObj = db.DBConnection()
                exists = vd.ifFileNameExists(dbObj.conn, fileName)
                print("RESULT ", exists)
                if not exists:
                    print(fileName + ' - File can be processed...')
                    # check for type of file
                    claim_type = xd.getTypeofClaim(file)
                    print("Claim Type ", claim_type)
                    if claim_type == cm.CLAIM_SUBMISSION:
                        # Process Claims XML
                        clm_header = xd.getClaimHeaderData(file)
                        clm_data = xd.getClaimData(file)

                        claimIdList = self.getProcessedClaimIds(clm_data)
                        clm_header['ClaimType'] = self.getClaimType(clm_data)
                        clm_header['Claims'] = ",".join(claimIdList)

                        # Write Claims to DB
                        ind.writeFileDetails(dbObj.conn, clm_header)

                        if clm_header['ClaimType'] == 'Resubmission':
                            print("This is of type Resubmission ---- ")
                            ind.writeResubMaster(dbObj.conn, clm_data, clm_header)
                            # txtarea.insert(END, '\n' + fileName + ' ReSubmit Claim written into DB Successfully...')
                            print('\n' + fileName + ' ReSubmit Claim written into DB Successfully...')
                        elif clm_header['ClaimType'] == 'Submission':
                            print("This is of type Submission ---- ")
                            ind.writeClaimMaster(dbObj.conn, clm_data, clm_header)
                            ind.writeClaimDiagnosis(dbObj.conn, clm_data)
                            ind.writeClaimActivity(dbObj.conn, clm_data)
                            ind.writeClaimActObs(dbObj.conn, clm_data)
                            # txtarea.insert(END, '\n' + fileName + ' Claim written into DB Successfully...')
                            print('\n' + fileName + ' Claim written into DB Successfully...')

                    elif claim_type == cm.REMITTANCE_ADVICE:
                        # Process Remittance XML
                        print('In Remittance -- ')
                        rmt_header = xd.getRemittanceHeaderData(file)
                        rmt_data = xd.getRemitData(file)

                        claimIdList = self.getProcessedClaimIds(rmt_data)
                        print(' final claim id list ', claimIdList)
                        rmt_header['Claims'] = ",".join(claimIdList)

                        # Write Remittance to DB
                        if len(claimIdList) > 0:
                            ind.writeFileDetails(dbObj.conn, rmt_header)
                            ind.writeRemitMaster(dbObj.conn, rmt_data, rmt_header)
                            ind.writeRemitActivity(dbObj.conn, rmt_data)

                            # txtarea.insert(END, '\n' + fileName + ' A total of ' + str(len(claimIdList)) + 'Remittance written into DB Successfully...')
                            print('\n' + fileName + ' A total of ' + str(
                                len(claimIdList)) + 'Remittance written into DB Successfully...')
                        else:
                            # txtarea.insert(END, '\n' + fileName + ' Remittance Not written into DB')
                            print('\n' + fileName + ' Remittance Not written into DB')
                else:
                    # txtarea.insert(END, '\n' + fileName + ' already exists in DB ...')
                    print(fileName + ' - File already processed ...')

            # clear xmlFileNames
            xmlFileNames.clear()

        else:
            # txtarea.insert(END, '\n' + 'No Files Selected...')
            print('No Files Selected for processing')